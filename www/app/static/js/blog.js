var blog = new Vue({
    el: '#blog',
    data: {
        id: location.pathname.split('/').pop(),
        comment: '',
        comments: [],
        message:''
    },
    filters: {
        marked: marked
    },
    methods: {
        submit: function() {
            var self = this;
            if (! self.comment.trim()) {
                return showAlert(self, '请输入评论内容！');
            }
            $.ajax({
                url: '/api/blog/' + self.id + '/comment',
                type: 'POST',
                data: {
                    content: self.comment,
                    time: (self.comments[0] && self.comments[0].created_at) || 0
                },
                success: function(data) {
                    if (data.error) {
                        return showAlert(self, data.message || data.error || data);
                    }
                    self.comment = '';
                    self.comments = data.comments.concat(self.comments);
                }
            });
        }
    },
    ready: function() {
        var self = this;
        $.ajax({
            url: '/api/blog/' + self.id + '/comments',
            success: function(data) {
                if (data.error) {
                    return alert(data.message || data.error || data);
                }
                self.comments = data.comments;
            }
        });
    }
});

var vm = new Vue({
    el: '#blog',
    data: {
        message: '',
        blog: {
            name: '',
            summary: '',
            content: ''
        }
    },
    computed: {
        method: function() {
            return location.pathname.slice(-5) === '/edit' ? 'PUT' : 'POST';
        },
        url: function () {
            return '/api/blog/' + ((this.method === 'PUT') ? getUrlParams('id') : '');
        }
    },
    ready: function () {
        if (this.method === 'PUT') {
            $.ajax({
                url: this.url,
                success: function(blog) {
                    vm.blog = blog;
                }
            })
        }
    },
    methods: {
        submit: function () {
            $.ajax({
                url: this.url,
                type: this.method,
                data: this.blog,
                success: function(data) {
                    if (data && data.error) {
                        return showAlert(vm, data.message || data.data || data);
                    }
                    return location.assign(location.pathname.split('manage')[0] + 'blog/' + data.id);
                }
            });
        }
    }
});


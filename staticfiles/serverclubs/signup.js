      function closeForm() {
            window.location.href = "{% url 'index' %}";
        }

        function showLoading() {
            document.getElementById('loading').style.display = 'block';
        }

        document.getElementById('signup-form').addEventListener('submit', function (e) {
            e.preventDefault();
            let formValid = validateForm();
            if (formValid) {
                document.getElementById('submitBtn').disabled = true;
                showLoading();  // Show loader
                this.submit();
            }
        });

        function validateForm() {
            const fields = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
            let valid = true;
            fields.forEach(field => {
                if (!field.value.trim()) {
                    field.style.border = '2px solid red';
                    valid = false;
                } else {
                    field.style.border = '';
                }
            });
            return valid;
        }
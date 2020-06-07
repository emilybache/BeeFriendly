<template>
    <div id="app" class="container py-4">
        <div class="row">
            <span>Sign up for our newsletter!</span>
            <div class="col-12">
                <form @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label>Name:
                            <input type="text" class="form-control"
                                   v-model="Name">
                        </label>
                    </div>

                    <div class="form-group">
                        <label>Email:
                            <input type="email" class="form-control"
                                   v-model="Email">
                        </label>
                    </div>

                    <div class="form-group">
                        <button :disabled="!formIsValid"
                                @click.prevent="onSubmit"
                                type="submit"
                                class="btn btn-primary">
                            Submit
                        </button>
                    </div>
                </form>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'NewsletterSignup',
        props: {

        },
        data: function () {
            return {
                Name: '',
                Email: ''
            }
        },
        methods: {
            onSubmit() {
                if (!this.formIsValid) return;
                console.log("form submit");
                axios
                    .post('http://localhost:3001/newsletter', { params: this.form })
                    .then(response =>   {
                        console.log('Form has been posted', response);
                    }).catch(err => {
                    console.log('An error occurred', err);
                });
            }
        },
        computed: {
            formIsValid() {
                return (
                    this.Name.length > 0 && this.Email.length > 0
                );
            }
        }

    }
</script>



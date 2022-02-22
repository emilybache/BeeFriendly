<template>
    <div id="app" class="container">
        <div class="row">
            <h2 class="mx-auto">Sign up for our newsletter!</h2>
            <div class="col-12">
                <form @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label>Name:
                            <input id="newsletter_name" type="text" class="form-control"
                                   v-model="Name">
                        </label>
                    </div>

                    <div class="form-group">
                        <label>Email:
                            <input id="newsletter_email" type="email" class="form-control"
                                   v-model="Email">
                        </label>
                    </div>

                    <div class="form-group">
                        <button id="newsletter_submit"
                                :disabled="!formIsValid"
                                @click.prevent="onSubmit"
                                type="submit"
                                class="btn btn-primary">
                            Submit
                        </button>
                    </div>
                </form>
            </div>
            <div id="newsletter_greeting" class="mx-auto">
                <section v-if="errored">
                    <p>We're sorry, we're not able to sign you up for the newsletter at the moment, please try again later.</p>
                </section>
                <section v-else>
                    <div v-if="loading">Loading...</div>
                    <div v-else>
                        <span>{{ greeting }}</span>
                    </div>
                </section>

            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'NewsletterSignup',
        props: {
            clientId: Number
        },
        data: function () {
            return {
                Name: '',
                Email: '',
                loading: false,
                errored: false,
                greeting: '',
            }
        },
        methods: {
            onSubmit() {
                if (!this.formIsValid) return;
                console.log("form submit");
                this.loading = true
                var self = this
                axios
                    .get('http://localhost:3000/sayHello/' + this.Name)
                    .then(response =>   {
                        console.log('Form has been posted', response);
                        self.greeting = response.data
                    }).catch(err => {
                        console.log('An error occurred', err);
                        self.errored = true
                    })
                    .finally( () => self.loading = false);
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

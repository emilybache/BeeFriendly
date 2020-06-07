<template>
    <div id="app" class="container py-4">
        <div class="row">
            <div class="col-12">
                <form @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label>
                            Size of garden:
                            <select v-model="garden_sizes.selected_garden_size">
                                <option v-for="(option, index) in garden_sizes.options" v-bind:key="index"
                                        v-bind:value="option.value">
                                    {{ option.text }}
                                </option>
                            </select>
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
            <div>
                <section v-if="errored">
                    <p>We're sorry, we're not able to calculate your score at the moment, please try again later.</p>
                </section>
                <section v-else>
                    <div v-if="loading">Loading...</div>
                    <div v-else>
                        <span>Your score: {{ score }}</span>
                    </div>
                </section>

            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'GardenQuizz',
        props: {

        },
        data: function () {
            return {
                garden_sizes: {
                    selected_garden_size: "",
                    options: [
                        {text: "Please select one", value: ""},
                        {text: "Windowbox", value: "windowbox"},
                        {text: "Balcony", value: "balcony"},
                        {text: "Small < 15 m2", value: "small"},
                        {text: "Medium < 50 m2", value: "medium"},
                        {text: "Large < 100 m2", value: "large"},
                        {text: "Extra Large > 100 m2", value: "xlarge"}
                    ]
                },
                score: "unknown",
                loading: false,
                errored: false,
                clientUUID: "1234",
                requestID: "request-1"
            }
        },
        methods: {
            onSubmit() {
                if (!this.formIsValid) return;
                this.loading = true
                var garden_data = {'selected_garden_size': this.garden_sizes.selected_garden_size}
                console.log("submitting garden data ")
                console.log(garden_data)
                const axios_instance = axios.create({
                    baseURL: 'http://localhost:3000',
                    timeout: 1000,
                    headers: {'jaeger-baggage': 'session=' + this.clientUUID + ', request=' + this.requestID}
                })
                var self = this
                axios_instance
                    .post('flower_scorer', garden_data)
                    .then(response =>   {
                        console.log('Form has been posted', response)
                        self.score = response.data["score"]
                    })
                    .catch(err => {
                        console.log('An error occurred', err)
                        this.errored = true
                    })
                    .finally( () => this.loading = false)
            }
        },
        computed: {
            formIsValid() {
                return (
                    this.garden_sizes.selected_garden_size.length > 0
                );
            }
        }

    }
</script>



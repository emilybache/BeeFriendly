<template>
    <div class="container mt-4">
        <div class="row">
            <div class="col-12">
                <form @submit.prevent="onSubmit">
                    <div class="form-group">
                        <label>
                            Size of garden:
                            <select id="select-garden-size" v-model="garden_sizes.selected_garden_size" class="selectpicker">
                                <option v-for="(option, index) in garden_sizes.options" v-bind:key="index"
                                        v-bind:value="option.value">
                                    {{ option.text }}
                                </option>
                            </select>
                        </label>
                    </div>
                    Check all the flowers that are blooming:
                    <div>
                        <div class="d-inline ml-2" v-for="flower in flowers" :key="flower.name">
                            <input :id="'checkbox_' + flower.name" class="flowerCheckbox" type="checkbox" v-model="checkedFlowers" :value="flower.name"/>
                            <label :id="'label_' + flower.name"
                                   :for="'checkbox_' + flower.name"
                                   class="flowerLabel"
                                   v-bind:style="{
                                       backgroundImage: 'url('+getImageUrl(flower)+')'
                                   }">

                            </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <button :disabled="!formIsValid"
                                @click.prevent="onSubmit"
                                type="submit"
                                class="btn btn-primary"
                                id="submit-garden-quizz"
                        >
                            Submit
                        </button>
                    </div>
                </form>
            </div>
            <div id="garden_advice" class="mx-auto">
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
            clientId: Number
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
                lastRequestID: 0,
                checkedFlowers: [],
                flowers: [
                    {name: "azalea", title: "Azalea"},
                    {name: "daisy", title: "Daisy"},
                    {name: "forsythia", title: "Forsythia"},
                    {name: "giant_daisy", title: "Giant Daisy"},
                    {name: "lilac", title: "Lilac"},
                    {name: "peony", title: "Peony"},
                    {name: "rhododendron", title: "Rhododendron"},
                    {name: "wild_strawberry", title: "Wild Strawberry"},
                ]
            }
        },
        methods: {
            onSubmit() {
                if (!this.formIsValid) return;
                this.loading = true
                var garden_data = {'selected_garden_size': this.garden_sizes.selected_garden_size,
                                   'selected_flowers': this.checkedFlowers}
                var jaeger_baggage = {'jaeger-baggage': 'session=' + this.clientId + ',request=garden_quizz' + this.getRequestID()}

                console.log("garden flowers: ")
                console.log(garden_data.selected_flowers)
                const axios_instance = axios.create({
                    baseURL: 'http://localhost:3004',
                    timeout: 1000,
                    headers: jaeger_baggage
                })
                var self = this
                axios_instance
                    .post('flower_scorer', garden_data)
                    .then(response =>   {
                        console.log('Form has been posted', response)
                        self.errored = false
                        self.score = response.data["score"]
                    })
                    .catch(err => {
                        console.log('An error occurred', err)
                        self.errored = true
                    })
                    .finally( () => self.loading = false)
            },
            getRequestID() {
                this.lastRequestID += 1
                return this.lastRequestID
            },
            getImageUrl(flower) {
                var images = require.context('../assets/', false, /\.jpg$/)
                return images('./' + flower.name + ".jpg")
            },
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
<style noscope>
    .flowerCheckbox {
      display:none;
    }
    .flowerLabel {
        border: solid 1px #00f;
        width: 100px;
        height: 100px;
        display: inline-block;
        cursor: pointer;
    }
    .flowerCheckbox:checked + .flowerLabel {
        border: solid 5px #00f;
    }
</style>

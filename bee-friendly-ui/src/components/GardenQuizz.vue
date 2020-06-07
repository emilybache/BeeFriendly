<template>
    <div id="app" class="container py-4">
        <div class="row">
            <div class="col-12">
                <form>
                    <div class="form-group">
                        <label>
                            Size of garden:
                            <select v-model="garden_sizes.selected_garden_size">
                                <option v-for="(option, index) in garden_sizes.options" v-bind:key="index" v-bind:value="option.value">
                                    {{ option.text }}
                                </option>
                            </select>
                        </label>

                    </div>

                    <div class="form-group">
                        <label>Name:</label>
                        <input type="text" class="form-control">
                    </div>

                    <div class="form-group">
                        <label>Email:</label>
                        <input type="email" class="form-control">
                    </div>

                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'HelloWorld',
        props: {
            msg: String
        },
        data: function () {
            return {
                garden_sizes: {
                    selected_garden_size: "",
                    options: [
                        { text: "Please select one", value: ""},
                        { text: "Windowbox", value: "windowbox"},
                        { text: "Balcony", value: "balcony"},
                        { text: "Small < 15 m2", value: "small"},
                        { text: "Medium < 50 m2", value: "medium"},
                        { text: "Large < 100 m2", value: "large"},
                        { text: "Extra Large > 100 m2", value: "xlarge"}
                    ]
                }
            }
        }

    }
</script>



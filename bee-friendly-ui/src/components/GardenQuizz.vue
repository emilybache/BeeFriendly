<template>
    <div id="app" class="container py-4">
        <div class="row">
            <div class="col-12">
                <form>
                    <div class="form-group">
                        <label>First Name:</label>
                        <input type="text" class="form-control">
                    </div>

                    <div class="form-group">
                        <label>Last Name:</label>
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
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }
</style>

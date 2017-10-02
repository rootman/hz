<template>
    <div class="main-app">
        <div class="container">

            <h2>Alle Urteile</h2>

            <div class="search-box">
                <i class="material-icons search-box__icon">search</i>
                <input type="text" v-model="query" class="input input--with-icon" placeholder="Search...">
            </div>

            <card-list :items="filteredItems" v-if="filteredItems.length > 0"></card-list>
            <div class="no-results" v-else>
                Sadly there are no results for your search.
            </div>

            <div class="grid">
                <div class="grid__item">
                    <h2>Arbeitsrecht</h2>
                    <div>
                        <card-list :items="arbeitsrechtItems" v-if="arbeitsrechtItems.length > 0"></card-list>
                        <div class="no-results" v-else>
                            Sadly there are no results for your search.
                        </div>
                    </div>
                </div>

                <div class="grid__item">
                    <h2>Mietrecht</h2>
                    <div>
                        <card-list :items="mietrechtItems" v-if="mietrechtItems.length > 0"></card-list>
                        <div class="no-results" v-else>
                            Sadly there are no results for your search.
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script src="./MainApp.js">
</script>

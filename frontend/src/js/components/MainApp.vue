<template>
    <div class="main-app">
        <header class="header">
            <div class="container">
                <div class="header__wrapper">
                    <div class="header__branding">
                        <i class="material-icons header__brandingicon">gavel</i>
                        iTrainee
                    </div>
                    <div class="header__slogan">
                        Let software do the boring work...
                    </div>
                </div>
            </div>
        </header>

        <div class="section section--search">
            <div class="container">
                <h1>Aktuelle Entscheide</h1>

                <div class="search-box">
                    <i class="material-icons search-box__icon">search</i>
                    <input type="text" v-model="query" class="input input--with-icon" placeholder="Suchen...">
                </div>

                <card-list :items="filteredItems" v-if="filteredItems.length > 0"></card-list>
                <div class="no-results" v-else>
                    Sadly there are no results for your search.
                </div>
            </div>
        </div>

        <div class="section section--dark">
            <div class="container">
                <div class="grid">
                    <div class="grid__item" v-for="area in areas">
                        <h2>{{area.name}}</h2>
                        <div>
                            <card-list :items="area.items" v-if="area.items.length > 0"></card-list>
                            <div class="no-results" v-else>
                                Sadly there are no results for your search.
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script src="./MainApp.js">
</script>

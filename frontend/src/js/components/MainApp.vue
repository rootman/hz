<template>
    <div class="main-app">
        <div class="container">

            <div class="search-box">
                <input type="text" v-model="query" class="input" placeholder="Search for Tags...">
            </div>

            <transition-group tag="ul" class="card-list" name="list-transition">
                <li class="card-list__item" v-for="item in filteredItems" :key="item.title">
                    <div class="card">
                        <div class="card__content">
                            {{item.title}}
                        </div>
                        <div class="card__tags">
                            <ul class="tag-list">
                                <li class="tag-list__item" v-for="tag in item.tags">
                                    <div class="tag">{{tag}}</div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </li>
            </transition-group>

        </div>
    </div>
</template>

<script src="./MainApp.js">
</script>

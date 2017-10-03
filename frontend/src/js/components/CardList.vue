<template>
    <transition-group tag="ul" class="card-list" name="list-transition">
        <li class="card-list__item" v-for="item in items" :key="item.title">
            <div class="card" :class="{'card--approved': item.approved}">
                <div class="card__header">
                    <action-list :item="item"></action-list>
                </div>
                <div class="card__comment">
                    <textarea class="card__commentarea" placeholder="Kommentar, Anweisung, ..." v-model="item.comment"></textarea>
                </div>
                <div class="card__body">
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
            </div>
        </li>
    </transition-group>
</template>

<script src="./CardList.js">
</script>

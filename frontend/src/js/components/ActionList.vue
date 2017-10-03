<template>
    <div class="action-list">
        <div class="action-list__item">
            <a href="#" class="action-list__link" v-if="!item.approved" target="_blank" @click.prevent="item.approved = true" title="Bestätigen">
                <i class="material-icons action-list__icon">check</i>
            </a>
            <a href="#" class="action-list__link" v-else target="_blank" @click.prevent="item.approved = false" title="Bestätigung zurückziehen">
                <i class="material-icons action-list__icon">close</i>
            </a>
        </div>
        <div class="action-list__item">
            <a href="#" class="action-list__link" target="_blank" title="Zur Webseite">
                <i class="material-icons action-list__icon">link</i>
            </a>
        </div>
        <div class="action-list__item">
            <a href="" class="action-list__link" @click.prevent="item.hidden = true" title="Verwerfen">
                <i class="material-icons action-list__icon">delete</i>
            </a>
        </div>
    </div>
</template>

<script src="./ActionList.js">
</script>

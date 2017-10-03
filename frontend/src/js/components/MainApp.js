//import items from '../data'
import itemData from '../../../../documents.json'
import CardList from './CardList.vue'
import areaData from '../areas.json'
import R from 'ramda'

let uid = 1
const items = itemData.map(item => ({
    ...item,
    hidden: false,
    comment: null,
    approved: false,
    departments: [],
    title: item.gegenstand || item.url,
    uid: uid++,
}))

export default {
    data() {
        return {
            items,
            query: '',
            areaData,
        }
    },
    computed: {
        visibleItems() {
            return this.items.filter(item => item.hidden !== true)
        },
        filteredItems() {
            return this.visibleItems.filter(item => this.matchTitle(this.query, item) || this.matchId(this.query, item) || this.matchTag(this.query, item))
        },
        areas() {
            return this.areaData.map(area => {
                return {
                    ...area,
                    items: this.visibleItems.filter(item => this.matchTags(area.tags, item.tags))
                }
            })
        }
    },
    methods: {
        matchTitle(query, item) {
            return item.title.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1
        },
        matchId(query, item) {
            return item.id.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1
        },
        matchTag(query, item) {
            return item.tags.filter(tag => tag.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1).length > 0
        },
        matchTags(areaTags, itemTags) {
            return R.intersection(
                areaTags.map(tag => tag.toLowerCase()),
                itemTags.map(tag => tag.toLowerCase()),
            ).length > 0
        },
    },
    components: {
        CardList
    }
}
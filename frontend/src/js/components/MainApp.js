import items from '../data'
import CardList from './CardList.vue'
import areaData from '../areas.json'

export default {
    data() {
        return {
            items,
            query: '',
            areaData,
        }
    },
    computed: {
        filteredItems() {
            return this.items.filter(item => this.matchTitle(this.query, item) || this.matchTag(this.query, item))
        },
        arbeitsrechtItems() {
            return this.items.filter(item => this.matchTitle('Arbeitsrecht', item) || this.matchTag('Arbeitsrecht', item))
        },
        mietrechtItems() {
            return this.items.filter(item => this.matchTitle('Mietrecht', item) || this.matchTag('Mietrecht', item))
        },
        areas() {
            return this.areaData.map(area => {
                return {
                    ...area,
                    items: this.items.filter(item => this.matchTags(area.tags, item))
                }
            })
        }
    },
    methods: {
        matchTitle(query, item) {
            return item.title.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1
        },
        matchTag(query, item) {
            return item.tags.filter(tag => tag.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1).length > 0
        },
        matchTags(tags, item) {
            return 1;
        },
    },
    components: {
        CardList
    }
}
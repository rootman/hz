import items from '../data'

export default {
    data() {
        return {
            items,
            query: '',
        }
    },
    computed: {
        filteredItems() {
            return this.items.filter(item => this.matchTitle(this.query, item) || this.matchTag(this.query, item))
        }
    },
    methods: {
        matchTitle(query, item) {
            return item.title.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1
        },
        matchTag(query, item) {
            return item.tags.filter(tag => tag.toLowerCase().indexOf(query.trim().toLowerCase()) !== -1).length > 0
        }
    }
}
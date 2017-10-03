import ActionList from './ActionList.vue'
import departments from '../departments'

export default {
    props: ['items'],
    data() {
        return {
            departments
        }
    },
    components: {
        ActionList
    },
    methods: {
        toggleDepartment(item, department) {
            if (item.departments.indexOf(department) !== -1) {
                item.departments = item.departments.filter(dep => dep !== department)
                return
            }

            item.departments.push(department)
        }
    }
}
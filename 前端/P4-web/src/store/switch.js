export default {
    state: {
        switchId: 0,
        Arr: {}
    },
    getters: {
    },
    mutations: {
        updateId(state, id) {
            console.log(id);
            state.switchId = id;
        },
        updateArr(state, Arr) {
            state.Arr = Arr
        }
    },
    actions: {

    },
    modules: {
    }
}
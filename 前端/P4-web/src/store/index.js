import { createStore } from 'vuex'
import flow from "./flow"
import switchs from "./switch"
export default createStore({
  modules: {
    flow: flow,
    switchs: switchs
  }
})

import store from '@/store';
import axios from 'axios';
const state = {
    switches:[]

}

const getters = {

}

const actions ={
}

const mutations = {
    setSwitches(state,res){
        state.switches.splice(0,state.switches.length); 
        res.forEach(ele => {
            state.switches.push({id:ele})
        });
        state.switches.sort(function(a,b){return a.id-b.id})
    }
}

export default {
    namespaced:true,
    getters,
    state,
    actions,
    mutations,
}
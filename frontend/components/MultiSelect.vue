<template>
  <div>
      <div class="select2-container select2-container-multi full-width multiselect">
        <multiselect
          class="form-control form-control-select textarea multiselect" 
          :class="{ 'has-error': showError }"
          @input="updateSelected"
          @close="blur">
        </multiselect>
      </div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
  components: {
    Multiselect
  },
  data () {
    return {
      value: "",
      options: true
    }
  }
}
</script>

<style lang="css" scoped>
.multiselect >>> .multiselect__tags {
    font-size: 14px;
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
}

.multiselect >>> .multiselect__select {
    font-size: 14px;
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
}
</style>

<style> 

* {
    font-size: 14px;
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
}
</style> 

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

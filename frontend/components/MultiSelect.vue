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
      value: "All Colleges",
      selected:"All Colleges",
      options: ["All Colleges", "Balliol College","Brasenose College", 
      "Christ Church","Corpus Christi College", "Exeter College", 
      "Harris Manchester College", "Hertford College", "Jesus College",
      "Keble College", "Lady Margaret Hall", "Lincoln College",
      "Magdalen College","Mansfield College","Merton College",
      "New College","Oriel College","Pembroke College", "The Queen's College",
      "Regent's Park College","St Anne's College","St Benet's Hall", 
      "St Catherine's College","St Edmund Hall","St Hilda's College",
      "St Hugh's College","St John's College","St Peter's College","Somerville College",
      "Trinity College","University College", "Wadham College", "Worcester College",
      "Wycliffe Hall"]
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

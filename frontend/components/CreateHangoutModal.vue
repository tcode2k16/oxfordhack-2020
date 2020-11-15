<template>
  <div class="modal">
    <div class="container">
      <div>
        <div class="center">
          <page-title >Create a new hangout</page-title>
        </div>
        <label for="fname">Location</label>
        <div id="gender-btns">
          <input v-model="location" type="radio" id="anywhere" name="location" value="anywhere" />
          <label for="anywhere">Anywhere</label>
       
          <input v-model="location" type="radio" id="christ" name="location" value="christ" />
          <label for="christ">Christ Church Meadow</label>
      
          <input v-model="location" type="radio" id="university" name="location" value="university" />
          <label for="university">University Parks</label>
     
          <input v-model="location" type="radio" id="port" name="location" value="port" />
          <label for="port">Port Meadow</label>
        </div>
        <br />
        <div id="info">
          <div>
            <label for="fname">Activity</label>
            <div id="gender-btns">
              <input v-model="activity" type="radio" id="anything" name="activity" value="anything" />
              <label for="anything">Anything</label>
              <input v-model="activity" type="radio" id="walk" name="activity" value="walk" />
              <label for="walk">Walk</label>
              <input v-model="activity" type="radio" id="run" name="activity" value="run" />
              <label for="run">Run</label>
              <input v-model="activity" type="radio" id="bike" name="activity" value="bike" />
              <label for="bike">Bike</label>
              <input v-model="activity" type="radio" id="sit" name="activity" value="sit" />
              <label for="sit">Sit</label>
            </div>
            <label for="dateTime">Date and time</label>
            <input type="text" id="dateTime" name="dateTime" v-model="time" />
            <label for="additional">Additional info</label>
            <input type="text" id="additional" name="additional"/>
          </div>
          <div>
            <label for="filter">I'd like to meet people from...</label>
            <multiselect v-model="collegeValue" :options="collegeOptions" :searchable="true" :close-on-select="false" :show-labels="false" placeholder="All colleges"></multiselect>
            <div class="row">
              <div id="gender-btns">
                <input v-model="cond_year" type="radio" id="undergrad" name="year" value="undergrad" />
                <label for="undergrad">Undergrad</label>
                <input v-model="cond_year" type="radio" id="masters" name="year" value="masters" />
                <label for="masters">Masters</label>
                <input v-model="cond_year" type="radio" id="phd" name="year" value="phd" />
                <label for="phd">PhD</label>
              </div>
              <multiselect v-model="yearValue" :options="yearOptions" :searchable="true" :close-on-select="false" :show-labels="false" placeholder="All years"></multiselect>
            </div>
            <multiselect v-model="departmentValue" :options="departmentOptions" :searchable="true" :close-on-select="false" :show-labels="false" placeholder="All departments"></multiselect>
            <div id="gender-btns">
              <input v-model="cond_gender" type="radio" id="anyone" name="gender" value="anyone" />
              <label for="anyone">Anyone</label>
              <input v-model="cond_gender" type="radio" id="male" name="gender" value="male" />
              <label for="male">Men</label>
              <input v-model="cond_gender" type="radio" id="female" name="gender" value="female" />
              <label for="female">Women</label>
              <input v-model="cond_gender" type="radio" id="nonbinary" name="gender" value="nonbinary" />
              <label for="nonbinary">Nonbinary</label>
            </div>
          </div>
        </div>
        <div id="buttons">
          <button @click="createHangout();close();">Create hangout</button>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
import Axios from "axios";
import PageTitle from "../components/PageTitle";
import Multiselect from 'vue-multiselect'
export default {
  name: "Modal",
  methods: {
  async createHangout() {
    let r = await Axios.post("/auth/publish", {
      time: "time",
      location: this.location,
      activity: this.activity,
      cond_name: "cond",
      cond_college: collegeValue,
      cond_department: departmentValue,
      cond_gender: "gend",
      cond_year: yearValue
    });
    if (!r.data.error) {
        this.notiOpen = true;
      }
    console.log(r.data);
  },
  close(event) {
      this.$emit("close");
    }
  },
  props: {
    value: {
      type: Boolean,
      default: true
    }
  },
  components: {
    "page-title": PageTitle,
    Multiselect
  },
  data () {
    return {
      time: "time",
      location: undefined,
      activity: undefined,
      cond_name: undefined,
      cond_college: undefined,
      cond_department: undefined,
      cond_gender: undefined,
      cond_year: undefined,

      collegeValue: "All College",
      collegeOptions: ["All College", "Balliol College","Brasenose College", 
      "Christ Church","Corpus Christi College", "Exeter College", 
      "Harris Manchester College", "Hertford College", "Jesus College",
      "Keble College", "Lady Margaret Hall", "Lincoln College",
      "Magdalen College","Mansfield College","Merton College",
      "New College","Oriel College","Pembroke College", "The Queen's College",
      "Regent's Park College","St Anne's College","St Benet's Hall", 
      "St Catherine's College","St Edmund Hall","St Hilda's College",
      "St Hugh's College","St John's College","St Peter's College","Somerville College",
      "Trinity College","University College", "Wadham College", "Worcester College",
      "Wycliffe Hall"],
      yearValue: "All years",
      yearOptions: ["All years", "1st year", "2nd year", "3rd year","4th year & up"],
      departmentValue: "All departments",
      departmentOptions: ["American Institute","Art","Classics","English Language and Literature","History","History of Art",
        "Linguistics, Philology & Phonetics","Medieval and Modern Languages","Music","Oriental Studies","Philosophy","Theology and Religion","Chemistry","Computer Science","e-Research Centre","Earth Sciences","Engineering Science",
        "Life Sciences Interface Doctoral Training Centre","Materials","Mathematics","Physics", "Plant Sciences", 
        "Statistics", "Zoology", "Biochemistry", "Clinical Medicine","Clinical Neurosciences",
        "Experimental Psychology","Medicine","Oncology", "Orthopaedics, Rheumatology and Musculoskeletal Sciences","Paediatrics", 
        "Pathology","Pharmacology", "Physiology, Anatomy & Genetics", "Population Health", "Primary Care Health Sciences", "Psychiatry", "Surgical Sciences", 
        "Women's & Reproductive Health", "Anthropology and Museum Ethnography", "Archaeology", "Business","Economics", 
        "Education", "Geography and the Environment", "Global and Area Studies", "Government", "International Development", "Internet Institute","Law","Oxford Martin School","Politics and International Relations", 
        "Social Policy and Intervention", "Sociology", "Continuing Education"]
            }
  },
  mounted() {
    this.collegeValue = "Any College";
    this.yearValue = "All year";
    this.departmentValue = "All departments";
  }
};
</script>
    
    
<style lang="css" scoped>
.modal {
  background-color: #fff;
  position: fixed;
  top: 10%;
  left: 10%;
  right: 10%;
  bottom: 10%;
  width: 100%;
  max-width: 1100px;
  border-radius: 5px;
  padding: 40px;
  border: 3px solid #428fea;
  z-index: 99;
}

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

#buttons {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
  max-width: 350px;
}

#buttons > button {
  margin-left: 20px;
  background-color: #428fea;
  color: #ffffff;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px;
  height: fit-content;

  cursor: pointer;
}

#gender-btns {
  display: flex;
  justify-content: flex-start;
  cursor: pointer;
  /* flex-wrap: wrap; */
  /* width: 100%; */
}
#gender-btns > button {
  /* margin-left: 20px;
  background-color: #428FEA;
  color: #FFFFFF;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px; */

  background: #eeeeee;
  border-radius: 5px;
  outline: none;
  border: none;
  /* height: 44px; */
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  /* padding: 5px; */
  padding-top: 5px;
  padding-bottom: 5px;
  cursor: pointer;
  /* width: 100%; */
}

#info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 70px;
  max-width: 1000px;
}

#info > div {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
  align-items: flex-start;
  white-space: nowrap;

  /* margin: 10px; */
  /* column-gap: 10px; */
}

.selected {
  background-color: #428fea !important;
  color: #ffffff;
}

input[type="radio"] {
  display: none;
}
input[type="radio"] + label {
  user-select: none;
  background: #eeeeee;
  border-radius: 5px;
  outline: none;
  border: none;
  /* height: 44px; */
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  /* padding: 5px; */
  padding-top: 5px;
  padding-bottom: 5px;
  margin-right: 10px;
  padding-left: 5px;
  padding-right: 5px;
}
input[type="radio"]:checked + label {
  background-color: #428fea !important;
  color: #ffffff;
}

label {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;

  color: #000000;
}

input {
  background: #eeeeee;
  border-radius: 5px;
  outline: none;
  border: none;
  /* height: 44px; */
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  /* padding: 5px; */
  padding-top: 5px;
  padding-bottom: 5px;
  width: 100%;
  max-width: 350px;
  padding-left: 10px;
  padding-right: 10px;
}

.center {
  margin: auto;
  width: 60%;
  padding: 10px;
  justify-content: center;
  text-align: center;
}
</style>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<template>
  <div>
    <v-card
      v-for="journal in journals"
      :key="journal.id"
      class="bg-grey-lighten-4 rounded-lg main-font my-10"
      elevation="5"
      width="600"
    >
      <v-col class="px-0">
        <v-row class="d-flex justify-space-between px-8 py-6" align="center">
          <div class="d-flex">
            <v-avatar>
              <v-img :src="journal.profile_image" />
            </v-avatar>
            <v-col class="py-0 px-0">
              <v-card-title>{{ journal.name }}</v-card-title>
              <v-card-subtitle>{{ journal.dateWhenMade }}</v-card-subtitle>
            </v-col>
          </div>
          <v-card-action>
            <v-btn variant="text"><v-icon>mdi-dots-horizontal</v-icon></v-btn>
            <v-btn
              variant="text"
              @click="deleteJournal(journal.id)"
              class="text-subtitle-1"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-action>
        </v-row>

        <v-card-text class="py-0">
          {{ journal.content }}
        </v-card-text>

        <v-col v-if="journal.content_image" class="py-3 px-0">
          <v-img
            cover
            height="450"
            max-width="600"
            :src="journal.content_image"
          />
        </v-col>

        <v-card-subtitle class="pt-5"> Share your journal to: </v-card-subtitle>
        <v-row class="py-6 px-7">
          <Button
            class="mr-5 bg-grey-lighten-2"
            elevation="5"
            :noSpacing="false"
            icon="mdi-facebook"
            >Facebook</Button
          >
          <Button
            class="mr-5 bg-grey-lighten-2"
            elevation="5"
            :noSpacing="false"
            icon="mdi-reddit"
            >Reddit</Button
          >
          <Button
            class="mr-5 bg-grey-lighten-2"
            elevation="5"
            :noSpacing="false"
            icon="mdi-instagram"
            >Instagram</Button
          >
        </v-row>
      </v-col>
    </v-card>
  </div>
</template>
  
<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const journals = ref([]);

const fetchJournalData = async () => {
  try {
    const response = await axios.get("/api/journals/");

    journals.value = response.data.map((journal) => ({
      ...journal,
    }));
  } catch (error) {
    console.error("error yawa");
  }
};

const deleteJournal = async (id) => {
  if (!confirm("Are you sure you want to delete your journal?")) return;

  try {
    await axios.delete(`/api/journals/${id}/`);
    journals.value = journals.value.filter((journal) => journal.id !== id);
  } catch (error) {
    console.error("Error deleting brad");
  }
};

onMounted(fetchJournalData);
</script>
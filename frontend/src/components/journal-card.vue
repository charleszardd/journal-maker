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
          <v-card-action class="d-flex">

            <v-menu transition="scale-transition">
              <template v-slot:activator="{ props }">
                <v-btn v-bind="props" variant="text">
                  <v-icon>mdi-dots-horizontal</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item @click="editJournal(journal)">
                  <v-list-item-title>Edit</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

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
          <v-img cover height="450" max-width="600" :src="journal.content_image" />
        </v-col>

        <v-card-subtitle class="pt-5"> Share your journal to: </v-card-subtitle>
        <v-row class="py-6 px-7">
          <Button class="mr-5 bg-grey-lighten-2" elevation="5" icon="mdi-facebook">Facebook</Button>
          <Button class="mr-5 bg-grey-lighten-2" elevation="5" icon="mdi-reddit">Reddit</Button>
          <Button class="mr-5 bg-grey-lighten-2" elevation="5" icon="mdi-instagram">Instagram</Button>
        </v-row>
      </v-col>
    </v-card>

    <v-dialog v-model="isEditDialogOpen" max-width="500px">
      <v-card>
        <v-card-title>Edit Journal</v-card-title>
        <v-card-text>
          <v-file-input v-model="editedJournal.profile_image" :prepend-icon="false" label="Your profile image"></v-file-input>
          <v-text-field v-model="editedJournal.name" label="Your name"></v-text-field>
          <v-textarea v-model="editedJournal.content" label="Content"></v-textarea>
          <v-file-input v-model="editedJournal.content_image" :prepend-icon="false" label="Content Image (Optional)"></v-file-input>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="isEditDialogOpen = false" variant="text">Cancel</v-btn>
          <v-btn @click="updateJournal" color="primary">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";



const journals = ref([]);
const isEditDialogOpen = ref(false);
const editedJournal = ref({ id: null, name: "", content: "", profile_image: null, content_image: null, });

const fetchJournalData = async () => {
  try {
    const response = await axios.get("/api/journals/");
    journals.value = response.data.sort((a, b) => b.id - a.id);
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

const editJournal = (journal) => {
  editedJournal.value = { ...journal };
  isEditDialogOpen.value = true;
};

const updateJournal = async () => {
  try {
    const formData = new FormData();
    formData.append("name", editedJournal.value.name);
    formData.append("content", editedJournal.value.content);

    if (editedJournal.value.profile_image instanceof File) {
      formData.append("profile_image", editedJournal.value.profile_image);
    }

    if (editedJournal.value.content_image instanceof File) {
      formData.append("content_image", editedJournal.value.content_image);
    }

    const response = await axios.put(`/api/journals/${editedJournal.value.id}/`, formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    const updatedJournal = response.data; 
    const index = journals.value.findIndex((j) => j.id === editedJournal.value.id);
    if (index !== -1) {
      journals.value[index] = updatedJournal; 
    }

    isEditDialogOpen.value = false;
  } catch (error) {
    console.error("Error updating journal brad", error);
  }
};

onMounted(fetchJournalData);
</script>

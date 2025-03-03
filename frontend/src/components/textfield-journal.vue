<template>
  <div>
    <v-card
      elevation="5"
      class="rounded-lg px-5 py-5 bg-grey-lighten-4"
      height="auto"
      width="600"
    >
      <v-row justify="center" align="center">
        <v-col cols="12" class="d-flex align-center justify-center">
          <v-avatar color="#212121" class="mr-3">
            <v-icon class="text-white">mdi-robot</v-icon>
          </v-avatar>

          <v-text-field
            variant="outlined"
            rounded
            label="What's on your mind, User?"
            @click="openModal"
            class="pt-5"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card>

    <v-dialog v-model="isModalOpen" max-width="600">
      <v-card class="rounded-lg py-2">
        <v-card-title class="text-center">Create Journal</v-card-title>
        <v-card-text>
          <v-file-input v-model="newJournal.profile_image"
          :prepend-icon="false"
          label="Enter a profile image"
          prepend-inner-icon="mdi-image"
          variant="outlined"
          ></v-file-input>
          <v-text-field
            v-model="newJournal.name"
            label="Enter your name"
             variant="outlined"
          ></v-text-field>
          <v-textarea
            v-model="newJournal.content"
            label="Anything you want to share"
             variant="outlined"
          ></v-textarea>
          <v-file-input
            v-model="newJournal.content_image"
            :prepend-icon="false"
            prepend-inner-icon="mdi-image"
            label="Your Content Image (Optional)"
             variant="outlined"
          ></v-file-input>
        </v-card-text>
        <v-card-actions class="pr-5">
          <v-btn color="grey" text @click="isModalOpen = false">Cancel</v-btn>
          <v-btn color="blue" @click="createJournal">Post</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script setup>
import { ref } from "vue";
import axios from 'axios'

const isModalOpen = ref(false);

const newJournal = ref({
  name: "",
  content: "",
  content_image: "",
  profile_image: null,
  content_image: null,
});

const openModal = () => {
  isModalOpen.value = true;
};

const createJournal = async () => {
  try {
    const formData = new FormData();
    formData.append("name", newJournal.value.name);
    formData.append("content", newJournal.value.content);
    
    if (newJournal.value.profile_image) {
      formData.append("profile_image", newJournal.value.profile_image);
    }
    if (newJournal.value.content_image) {
      formData.append("content_image", newJournal.value.content_image);
    }

    const response = await axios.post("/api/journals/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    isModalOpen.value = false;
    newJournal.value = { name: "", content: "", profile_image: null, content_image: null };
  } catch (error) {
    console.error("Failed to create journal:", error);
  }
};
</script>

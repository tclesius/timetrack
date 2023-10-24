import {defineStore} from "pinia";
import {ref} from "vue";
import {DefaultService} from "@/client";

export const useTimeStore = defineStore('time', () => {
    const buttonText = ref("")
    const data = ref({
        message: "",
        start_timestamp: null,
        end_timestamp: null,
        time_since_start: "",
        current_date: ""
    })

    async function fetchData(){
        const response = await DefaultService.getStatsLogStatsGet()
        data.value.message = response.message
        data.value.start_timestamp = response.start_timestamp
        data.value.end_timestamp = response.end_timestamp
        buttonText.value = (data.value.end_timestamp === null && data.value.start_timestamp !== null) ? "Stamp Out" : "Stamp In"
    }

    async function stampInOut() {
        const response = await DefaultService.postStampinoutLogStampinoutPost()
        data.value.message = response.message
        data.value.start_timestamp = response.start_timestamp
        data.value.end_timestamp = response.end_timestamp
        buttonText.value = (data.value.end_timestamp === null && data.value.start_timestamp !== null) ? "Stamp Out" : "Stamp In"
    }

    function refreshDate() {
        data.value.current_date = new Date().toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        });
    }

    function refreshTimer() {
        // Calculate the time elapsed since start_timestamp
        if (data.value.end_timestamp === null && data.value.start_timestamp !== null) {
            const startTimestamp = new Date(data.value.start_timestamp);
            const now = new Date();
            const timeDifference = now.getTime() - startTimestamp.getTime();

            // Calculate hours, minutes, and seconds
            const hours = Math.floor(timeDifference / 3600000);
            const minutes = Math.floor((timeDifference % 3600000) / 60000);
            const seconds = Math.floor((timeDifference % 60000) / 1000);

            // Format hours, minutes, and seconds with leading zeros
            const formattedHours = hours.toString()
            const formattedMinutes = minutes.toString().padStart(2, '0');
            const formattedSeconds = seconds.toString().padStart(2, '0');

            data.value.time_since_start = `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
            refreshDate();
        } else {
            data.value.time_since_start = '0:00:00';
            refreshDate();
        }
}

    return {stampInOut, fetchData, refreshTimer, data, buttonText}
})

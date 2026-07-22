import api from "./api";

export async function getCareerHistory() {

    const response = await api.get(
        "/career-history/"
    );

    return response.data;

}
import { SERVER_BASE_URL } from "@/consts"

export class FormRepository {
  constructor() {}

  async sendData(endpoint: string, formData: Record<string, unknown>) {
    try {
      const response = await fetch(`${SERVER_BASE_URL}/${endpoint}`, {
        mode: "no-cors",
        method: "POST",
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json"
        }
      })
      if (!response.ok) throw new Error("There was an error with the request. Please try again.")

      const data = await response.json()
      return { success: data.success, message: data.message }
    } catch (error) {
      throw new Error(`There was an error getting the data: ${error}`)
    }
  }
}

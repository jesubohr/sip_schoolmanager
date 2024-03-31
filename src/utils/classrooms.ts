import { SERVER_BASE_URL } from "@/consts"

export async function getClassroomOptions() {
  try {
    const response = await fetch(`${SERVER_BASE_URL}/schoolmanager/classrooms/get_all`, {
      mode: "no-cors",
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
    if (!response.ok) throw new Error("Failed to fetch classrooms")
    const data = await response.json()
    return data.map((classroom: { id: number, name: string }) => ({
      value: classroom.id,
      label: classroom.name
    }))
  } catch (error) {
    console.error(error)
    return []
  }
}

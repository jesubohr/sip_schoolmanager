import { type Form } from "@/models/form"
import { createElement } from "@/utils"

export class FormRender {
  #form: Form

  constructor(form: Form) {
    this.#form = form
  }

  renderForm(containerId: string) {
    const formContainer = document.getElementById(containerId)
    if (!formContainer) throw new Error("Container not found")

    const formElement = this.#createForm()
    const formStatus = this.#createFormStatus()
    const fields = this.#createFields()
    const submitButton = this.#createSubmitButton()
    const fieldsContainer = createElement("div", { class: "fields-container" })

    fields.forEach((field) => fieldsContainer.appendChild(field))
    formElement.appendChild(formStatus)
    formElement.appendChild(fieldsContainer)
    formElement.appendChild(submitButton)
    formElement.onsubmit = (event) => {
      event.preventDefault()
      this.#form.submit()
    }
    formContainer.appendChild(formElement)
  }

  setError(fieldId: string, message: string) {
    const errorElement = document.querySelector(`#${fieldId} .error-message`)
    if (errorElement) errorElement.textContent = message
  }

  setStatus(success: boolean, message: string) {
    const formStatus = document.querySelector(".form-status")
    const statusMessage = formStatus?.querySelector(".status-message")
    if (statusMessage) statusMessage.textContent = message
    formStatus?.setAttribute("data-status", success ? "success" : "error")
  }

  // Render Methods
  #createForm() {
    const formElement = createElement("form", {
      method: this.#form.method,
      action: this.#form.action
    })
    return formElement
  }

  #createFormStatus() {
    const formStatus = createElement("div", { class: "form-status", "data-status": "" })
    const statusMessage = createElement("p", { class: "status-message" })
    const closeButton = createElement("button", { class: "close-button" }, "×")

    closeButton.onclick = () => formStatus.remove()
    formStatus.appendChild(statusMessage)
    formStatus.appendChild(closeButton)
    return formStatus
  }

  #createFields() {
    return this.#form.inputs.map((field) => {
      const labelElement = createElement(
        "label",
        { for: field.id },
        field.label
      )
      const inputElement = createElement("input", {
        id: field.id,
        type: field.type,
        name: field.name,
        placeholder: field.placeholder ?? "",
        value: field.value ?? "",
        required: `${field.required}`
      })
      const errorElement = createElement("p", { class: "error-message" })

      inputElement.onchange = (ev: Event) => this.setError((ev.target as HTMLInputElement).id, "")
      labelElement.appendChild(inputElement)
      labelElement.appendChild(errorElement)
      return labelElement
    })
  }

  #createSubmitButton() {
    const button = createElement("button", { type: "submit" }, "Submit")
    return button
  }
}

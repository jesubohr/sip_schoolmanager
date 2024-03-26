import type { InputField } from "@/types"
import { FormFactory } from "@/factory/form-factory"
import { FormController } from "@/controllers/form-controller"
import { FormRender } from "@/render/form-render"
import { VALIDATORS } from "@/utils/validators"

const studentFormInputs: InputField[] = [
  {
    type: "text",
    id: "firstName",
    name: "firstName",
    label: "First Name",
    placeholder: "Enter your firstname",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty]
  },
  {
    type: "text",
    id: "lastName",
    name: "lastName",
    label: "Last Name",
    placeholder: "Enter your lastname",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty]
  },
  {
    type: "date",
    id: "birthdate",
    name: "birthdate",
    label: "Date of Birth",
    placeholder: "Enter your date of birth",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isDate]
  },
  {
    type: "email",
    id: "email",
    name: "email",
    label: "Email",
    placeholder: "Enter your email",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty, VALIDATORS.isEmail]
  },
  {
    type: "tel",
    id: "phone",
    name: "phone",
    label: "Phone",
    placeholder: "Enter your phone number",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty, VALIDATORS.isPhone]
  }
]

export function initRegisterForm() {
  const formFactory = new FormFactory()
  const formController = new FormController()

  const studentForm = formFactory.buildForm({
    method: "POST",
    action: "/register",
    inputs: studentFormInputs,
    onSubmit: (form) => {
      formController.submitForm(form)
    }
  })

  const formRender = new FormRender(studentForm)
  formRender.renderForm("form-container")
}

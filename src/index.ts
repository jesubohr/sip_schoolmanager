import type { InputField } from "@/types"
import { FormFactory } from "@/factory/form-factory"
import { FormController } from "@/controllers/form-controller"
import { FormRender } from "@/render/form-render"
import { VALIDATORS } from "@/utils/validators"
import { getClassroomOptions } from "@/utils/classrooms"

const studentFormInputs: InputField[] = [
  {
    type: "text",
    id: "firstName",
    name: "firstName",
    label: "Nombres",
    placeholder: "Ingresa tus nombres",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty]
  },
  {
    type: "text",
    id: "lastName",
    name: "lastName",
    label: "Apellidos",
    placeholder: "Ingresa tus apellidos",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty]
  },
  {
    type: "date",
    id: "birthdate",
    name: "birthdate",
    label: "Fecha de nacimiento",
    placeholder: "Ingresa tu fecha de nacimiento",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isDate]
  },
  {
    type: "email",
    id: "email",
    name: "email",
    label: "Correo electrónico",
    placeholder: "Ingresa tu correo electrónico",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty, VALIDATORS.isEmail]
  },
  {
    type: "number",
    id: "phone",
    name: "phone",
    label: "Teléfono",
    placeholder: "Ingresa tu teléfono",
    required: true,
    validators: [VALIDATORS.required, VALIDATORS.isEmpty, VALIDATORS.isPhone]
  }
]

export async function initRegisterForm() {
  const formFactory = new FormFactory()
  const formController = new FormController()
  const classroomOptions = await getClassroomOptions()

  studentFormInputs.push({
    type: "select",
    id: "classroomId",
    name: "classroomId",
    label: "Salón",
    placeholder: "Selecciona el salón",
    value: classroomOptions,
    required: true,
    validators: [VALIDATORS.required]
  })

  const studentForm = formFactory.buildForm({
    method: "POST",
    action: "schoolmanager/students/create",
    inputs: studentFormInputs,
    onSubmit: async (form) => {
      await formController.submitForm(form)
    }
  })

  const formRender = new FormRender(studentForm)
  formRender.renderForm("form-container")
}

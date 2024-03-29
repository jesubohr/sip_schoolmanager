import { describe, test, expect, vi } from "vitest"
import { FormRepository } from "@/repository/form-repository"
import { FormFactory } from "@/factory/form-factory"
import { createElement } from "@/utils/dom"

const createElementMock = vi.fn((tagName: string) => ({
  id: "",
  tagName: tagName.toUpperCase(),
  textContent: "",
  setAttribute(key: "id", value: string) {
    this[key] = value
  }
}))
vi.stubGlobal("document", { createElement: createElementMock })

describe("FormRepository", () => {
  test("should send data to the server", async () => {
    const formRepository = new FormRepository()
    const endpoint = "test"
    const formData = { data: "test" }
    const response = await formRepository.sendData(endpoint, formData)
    expect(response).toEqual({
      success: true,
      message: `Data ${formData} sent successfully`
    })
  })
})

describe("FormFactory", () => {
  test("should create a form", () => {
    const inputs = [
      {
        type: "text",
        id: "firstName",
        name: "firstName",
        placeholder: "Ingresa tus nombres",
        required: true,
        validators: []
      },
      {
        type: "text",
        id: "lastName",
        name: "lastName",
        placeholder: "Ingresa tus apellidos",
        required: true,
        validators: []
      }
    ]
    const formFactory = new FormFactory()
    const form = formFactory.buildForm({
      method: "POST",
      action: "test",
      inputs: inputs,
      onSubmit: () => {}
    })
    expect(form).toBeDefined()
    expect(form.method).toBe("POST")
    expect(form.action).toBe("test")
    expect(form.inputs).toEqual(inputs)
  })
})

describe("createElement", () => {
  test("should create a div element", () => {
    const element = createElement("div", { id: "test" }, "Test")
    expect(element.tagName).toBe("DIV")
    expect(element.id).toBe("test")
    expect(element.textContent).toBe("Test")
  })
})

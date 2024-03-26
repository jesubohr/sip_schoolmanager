export const VALIDATORS = {
  required: (value: string, name?: string) => {
    return {
      isValid: value != null,
      message: `The ${name ? name : "field"} is required`
    }
  },
  isEmpty: (value: string, name?: string) => {
    return {
      isValid: value !== "",
      message: `The ${name ? name : "value"} cannot be empty`
    }
  },
  isEmail: (value: string) => {
    return {
      isValid: /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value),
      message: "The email is not valid"
    }
  },
  isPhone: (value: string) => {
    return {
      isValid: /^\+?\d{0,3}\d{10}$/.test(value),
      message: "The phone number is not valid"
    }
  },
  isDate: (value: string) => {
    const dateObject = new Date(value)
    return {
      isValid: dateObject instanceof Date && !isNaN(dateObject.getTime()),
      message: "The date is not valid"
    }
  }
}

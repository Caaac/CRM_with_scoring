export default class Api {
  static ABSTRACT_MARKER = Symbol('abstract-field');
  static API_BASE_PATH = "/api/v1/";
  
  static _relation = Api.ABSTRACT_MARKER;

  constructor() {
    
    if (new.target === Api) {
      throw new Error("Cannot instantiate abstract class");
    }

    if (this._relation === Api.ABSTRACT_MARKER) {
      throw new Error(`Поле 'relation' должно быть переопределено`);
    }
  }

  static get relation() {
    return this._relation;
  }
}
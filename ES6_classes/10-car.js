export default class Car {
  constructor(brand, model, color) {
    this._brand = brand;
    this._model = model;
    this._color = color;
  }


  toString() {
    return `TestCar - ${this._brand} ${this._model} ${this._color}`;
  }  
  
    cloneCar() {
    return new Car(this._brand, this._model, this._color);
  }
}
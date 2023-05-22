import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlquilarCanchaComponent } from './alquilar-cancha.component';

describe('AlquilarCanchaComponent', () => {
  let component: AlquilarCanchaComponent;
  let fixture: ComponentFixture<AlquilarCanchaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlquilarCanchaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AlquilarCanchaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

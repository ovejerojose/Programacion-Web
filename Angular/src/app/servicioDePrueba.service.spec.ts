import { TestBed } from '@angular/core/testing';

import { ServicioDePrueba } from './servicioDePrueba.service';

describe('ServicioDePrueba', () => {
  let service: ServicioDePrueba;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServicioDePrueba);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

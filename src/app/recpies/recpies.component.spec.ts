import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecpiesComponent } from './recpies.component';

describe('RecpiesComponent', () => {
  let component: RecpiesComponent;
  let fixture: ComponentFixture<RecpiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RecpiesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecpiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

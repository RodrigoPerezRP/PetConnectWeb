import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from '../../../services/auth/auth-service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-register',
  imports: [ReactiveFormsModule],
  templateUrl: './register.html',
  styles: ``
})
export class Register {

  constructor(private authService: AuthService, private router: Router){}

  formRegister = new FormGroup({
    username: new FormControl<string>(''),
    last_name: new FormControl<string>(''),
    email: new FormControl<string>(''),
    password: new FormControl<string>(''),
  })

  onRegister(){
    this.authService.register(this.formRegister.value).subscribe({
      next: res => {
        this.router.navigate(['/auth/login'])
      },
      error: err => { 
        console.log(err)
      }
    })
  }

}

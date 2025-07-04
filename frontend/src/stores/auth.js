/* Vue */
import { ref } from "vue";
/* Pinia */
import { defineStore } from "pinia";
import { helperStore } from "./helper";

export const authStore = defineStore("auth", () => {
  const helper = helperStore()

  /* public */
  const isAuth = ref(true);
  /* private */
  const authTimer = ref(null);

  const initTimer = () => {
    console.log('initTimer', localStorage.getItem('authTimer'));
    if (localStorage.getItem('authTimer'))
      startTimer()
  }

  const login = (authData) => {
    Rest.callMethod(
      'auth.login',
      {
        login: authData.login,
        password: authData.password
      },
      (r) => {
        switch (r.status) {
          case 200:
            setToken(r.data.access, r.data.refresh)
            isAuth.value = true
            startTimer()
            break;
          case 400:
            // errorMessage.value = 'Неверный логин или пароль'
            break;
          default:
            // helper.errorToast('При попытке авторизации пошло что-то не так')
            break;
        }

        console.log(1, r);
      }
    )
  }

  const setToken = (access, refresh) => {
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  }

  const startTimer = (interval = 14) => {
    localStorage.removeItem('authTimer')

    authTimer.value = setInterval(() => {
      console.log('authTimer');
      Rest.callMethod(
        'auth.refresh',
        {refresh: localStorage.getItem('refreshToken')},
        (r) => {
          if (r.status == 200) {
            setToken(r.data.access, r.data.refresh)
          }
        }
      )
    }, interval * 60 * 1000)

    localStorage.setItem('authTimer', authTimer.value);
  }

  const stopTimer = () => {
    clearInterval(authTimer.value)
  }

  return {
    /* Store vars */
    isAuth,
    /* Store methods */
    login,
    initTimer,
    stopTimer
  };
});

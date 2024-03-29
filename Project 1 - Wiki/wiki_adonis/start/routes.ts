/*
|--------------------------------------------------------------------------
| Routes file
|--------------------------------------------------------------------------
|
| The routes file is used for defining the HTTP routes.
|
*/

import router from '@adonisjs/core/services/router'
const EntriesController = () => import('#controllers/entries_controller')

router.get('/', [EntriesController, 'index']).as('home')

router.get('/wiki/:slug', [EntriesController, 'show']).as('entries.show')

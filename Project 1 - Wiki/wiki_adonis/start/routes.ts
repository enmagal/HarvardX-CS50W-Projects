/*
|--------------------------------------------------------------------------
| Routes file
|--------------------------------------------------------------------------
|
| The routes file is used for defining the HTTP routes.
|
*/

import { Exception } from '@adonisjs/core/exceptions'
import router from '@adonisjs/core/services/router'
import app from '@adonisjs/core/services/app'
import fs from 'node:fs/promises'
import { MarkdownFile } from '@dimerapp/markdown'
import { toHtml } from '@dimerapp/markdown/utils'

router.on('/').render('pages/home').as('home')

router
  .get('/wiki/:title', async (ctx) => {
    const url = app.makeURL(`resources/entries/${ctx.params.title}.md`)
    try {
      const file = await fs.readFile(url, 'utf8')
      const md = new MarkdownFile(file)

      await md.process()

      const entry = toHtml(md).contents

      ctx.view.share({ entry, md })
    } catch (error) {
      throw new Exception(`Could not find the movie called ${ctx.params.slug}`, {
        code: 'E_NOT_FOUND',
        status: 404,
      })
    }
    return ctx.view.render('pages/entry/show')
  })
  .as('entries.show')

import Entry from '#models/entry'
import { HttpContext } from '@adonisjs/core/http'

export default class EntriesController {
  async index({ view }: HttpContext) {
    const entries = await Entry.all()

    return view.render('pages/home', { entries })
  }

  async show({ view, params }: HttpContext) {
    const entry = await Entry.find(params.slug)
    return view.render('pages/entry/show', { entry })
  }
}

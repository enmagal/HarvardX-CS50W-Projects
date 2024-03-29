import WikiService from '#services/wiki_service'
import { toHtml } from '@dimerapp/markdown/utils'

export default class Entry {
  declare slug: string

  declare content: string

  static async all() {
    const slugs = await WikiService.getSlugs()
    const entries: Entry[] = []

    for (const slug of slugs) {
      const movie = await this.find(slug)
      entries.push(movie)
    }

    return entries
  }

  static async find(slug: string) {
    const md = await WikiService.read(slug)
    const entry = new Entry()

    entry.slug = slug
    entry.content = toHtml(md).contents

    return entry
  }
}

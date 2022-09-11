/** @type {import('./$types').PageLoad} */
export function load({ params }) {
  return {
      role: params.slug
  };
}
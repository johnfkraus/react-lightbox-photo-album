import type { Photo } from "react-photo-album";

// adapted from:
const breakpoints = [1080, 640, 384, 256, 128, 96, 64, 48];

const bucket = "https://photo-album-22101.s3.us-east-1.amazonaws.com/srcset/"

function imageLink(path: string, width: number, height: number, size: number, extension: string) {
  return `${bucket}${path}.${width}x${height}.${size}w.${extension}`;
}

const photos = [
  // see 'filenames.md' for tips on how to refer to photos in this list

  { src: "meeks.3684.3024x4032.jpg", alt: "Meeks" },
  { src: "bronze.3623.1493x1613.jpg", alt: "Bronze figurines" },
  { src: "Engelhartszell_an_der_Donau_Innviertel_Austria.1000.4032x3024.jpg", alt: "Engelhartszell_an_der_Donau_Innviertel_Austria" },
  { src: "amery.3611.3024x4032.jpg", alt: "Amery, Wisconsin, vase, 1987" },
  { src: "birdhouse.7943.3024x4032.jpg", alt: "Birdhouse"},
  // { src: "annapolis.6702.3024x4032.jpg", alt: "Sailing on a schooner in Annapolis, Maryland" },
  // { src: "bronze.3623.1493x1613.jpg", alt: "Bronze figurines" },
  // { src: "buffalo.7161.4032x3024.jpg", alt: "South Dakota buffalo" },
  // { src: "dino-balloon.5224.3024x4032.jpg", alt: "Dinosaur balloon" },
  // { src: "meeks-book.0776.4032x3024.jpg", alt: "Meeks reading" },
  //
  // { src: "meeks.3A95.1141x642.jpg", alt: "Meeks" },
  // { src: "meeks.693245.3024x4032.jpg", alt: "Meeks" },
  // { src: "meeks.7597.3024x4032.jpg", alt: "Meeks the Cat" },
  // { src: "meeks.8237.3024x4032.jpg", alt: "Meeks" },
  // { src: "painted-stone.6872.4032x3024.jpg", alt: "Painted stone" },
  // { src: "weenie-beenie.5954.4032x3024.jpg", alt: "Weenie Beenie" },
  // { src: "sea-turtle.333.5568x4176.jpg", alt: "Sea Turtle, Puerto Rico"},
  // { src: "meeks.8143.2400x3600.jpg", alt: "Meeks" },
  // { src: "dishes.8073.4032x3024.jpg", alt: "Dishes"},

  // { src: "palace.8004.4032x3024.jpg", alt: "Nymphenburg Palace, Munich" },
  // { src: "hotel.8016.3024x4032.jpg", alt: "Munich hotel" },
  // { src: "frank-and-veronica.0001.1600x1200.jpeg", alt: "Frank and Veronica" },
  // { src: "emyla.7743.4032x3024.jpeg", alt: "Emyla" },
  // { src: "postcards.7742.3024x4032.jpg", alt: "Postcards" },
  // { src: "dishes.8073.4032x3024.jpg", alt: "Dishes"},

].map(({ src, ...rest }) => {
  console.log('src = ' + src);
  const matcher = src.match(/^(.*)\.(\d+)x(\d+)\.(.*)$/)!;

  const path = matcher[1];
  const width = Number.parseInt(matcher[2], 10);
  const height = Number.parseInt(matcher[3], 10);
  const extension = matcher[4];

  return {
    src: imageLink(path, width, height, width, extension),
    width,
    height,
    // OPTIONAL:
    srcSet: breakpoints.map((breakpoint) => ({
      src: imageLink(path, width, height, breakpoint, extension),
      width: breakpoint,
      height: Math.round((height / width) * breakpoint),
    })),
    ...rest,
  } as Photo;
});

export default photos;

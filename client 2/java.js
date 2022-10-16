const helloWorld = async () => {
  const got = await fetch("http://127.0.0.1:8000/");
  const info = await got.json();
  console.log(info);
};

const data = async () => {
  const got = await fetch("http://127.0.0.1:8000/objects");
  const info = await got.json();
  console.log(info);
  console.log(info[0]["image"]["src"]);
  const src = info[0]["image"]["src"];
  const height = info[0]["image"]["height"];
  console.log(height);
  const width = info[0]["image"]["width"];
  console.log(width);
  const img = document.createElement("img");
  img.src = src;
  img.style.height = height;
  img.style.width = width;
  document.getElementById("body").appendChild(img);
};

const correct_artist = async () => {
  const got = await fetch("http://127.0.0.1:8000/object");
  const info = await got.json();
  const name = info["title"];
};

const sendDate = async () => {
  const pic_date_guess = $("#year_made").val();
  const post = async () => {
    const rawResponse = await fetch("http://127.0.0.1:8000/date", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ date: pic_date_guess }),
    });
    const content = await rawResponse.json();
    const remainder = content["remainder"];
    const real_date = content["date"];
    if (pic_date_guess == real_date) {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You guessed correctly with: " + real_date
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    } else {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You were off by " + remainder + " the real date is " + real_date
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    }
  };
  post();
};

const sendArtist = async () => {
  const artist_guess = $("#artist").val();
  console.log(artist_guess);
  const post = async () => {
    const rawResponse = await fetch("http://127.0.0.1:8000/artist", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ artist: artist_guess }),
    });
    const content = await rawResponse.json();
    const got = await fetch("http://127.0.0.1:8000/object");
    const info = await got.json();
    const real_artist = info["title"];
    if (real_artist == artist_guess) {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You guessed correctly with: " + real_artist
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    } else {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You were incorrect with " +
          artist_guess +
          " the real artist is " +
          real_artist
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    }
  };
  post();
};

const sendStyle = async () => {
  const style_guess = $("#style").val();
  console.log(style_guess);
  const post = async () => {
    const rawResponse = await fetch("http://127.0.0.1:8000/style", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ style: style_guess }),
    });
    const content = await rawResponse.json();
    const real_style = content["style"];
    if (style_guess == real_style) {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You guessed correctly with: " + real_style
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    } else {
      const p = document.createElement("p");
      const text = document.createTextNode(
        "You were off with " + style_guess + " the real style is " + real_style
      );
      p.appendChild(text);
      const element = document.getElementById("result");
      element.appendChild(p);
    }
  };
  post();
};

const showQuestion = async () => {
  const result = $('input[name="game"]:checked').val();
  data();
  if (result == "date") {
    $("#the_year").show();
  } else if (result == "artist") {
    $("#the_artist").show();
  } else {
    $("#the_style").show();
  }
};

function test() {
  console.log("good");
  const pic_date_guess = $("#year_made").val();
  console.log(pic_date_guess);
}

$(document).ready(() => {
  $("#year_submit").click(sendDate);
  $("#artist_submit").click(sendArtist);
  $("#style_submit").click(sendStyle);
  $("#choice_submit").click(showQuestion);
  $("#the_year").hide();
  $("#the_artist").hide();
  $("#the_style").hide();
});

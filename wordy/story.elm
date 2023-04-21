-- Press a button to generate a random number between 1 and 6.
--
-- this is broken
--

import Browser
import Html exposing (..)
import Html.Events exposing (..)
import Random

-- constants

forenames = ["Matthew","Mark","Luke","John"]
surnames = ["Smith","White","Black","Ausgetzin"]
verbs = ["went","left","liked","loved","ate"]
nouns = ["car","ship","road","house","villa"]

random_name =
  Random.list forenames ++ Random.list surnames

-- MAIN


main =
  Browser.element
    { init = init
    , update = update
    , subscriptions = subscriptions
    , view = view
    }



-- MODEL


type alias Model =
  { dieFace : Int
  }


init : () -> (Model, Cmd Msg)
init _ =
  ( Model 0
  , Cmd.none
  )



-- UPDATE


type Msg
  = Roll
  | NewFace Int


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Roll ->
      ( model
      , Random.generate NewFace (Random.int 1 60)
      )

    NewFace newFace ->
      ( Model newFace
      , Cmd.none
      )



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none



-- VIEW

span_text = "span text"

view : Model -> Html Msg
view model =
  div []
    [ h1 [] [ text (String.fromInt model.dieFace) ]
    , button [ onClick Roll ] [ text "Roll" ]
    , p [] [text span_text]
    ]

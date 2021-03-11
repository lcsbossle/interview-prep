defmodule Solution do
  def newYearChaos(q) do
    chaotic_map = q |> Enum.with_index(1) |> Enum.map(&isChaotic/1)

    case Enum.member?(chaotic_map, true) do
      true ->
        IO.puts("Too chaotic")

      false ->
        q
        |> Enum.reverse()
        |> countBribes
        |> IO.puts()
    end
  end

  defp countBribes(q) when length(q) == 1, do: 0

  defp countBribes(q) do
    [i | rest] = q

    times_bribed =
      rest |> Enum.slice(0..max(length(q), i + 2)) |> Enum.filter(fn x -> x > i end) |> length

    times_bribed + countBribes(rest)
  end

  defp isChaotic({initial, final}) when initial > final + 2, do: true
  defp isChaotic({_initial, _final}), do: false

  def processData(data) when length(data) == 2 do
    [_n | [q]] = data

    q
    |> String.split(" ")
    |> Enum.map(fn n -> String.to_integer(n) end)
    |> newYearChaos
  end

  def processData(data) do
    [_n | [q | remaining_data]] = data

    q
    |> String.split(" ")
    |> Enum.map(fn n -> String.to_integer(n) end)
    |> newYearChaos

    processData(remaining_data)
  end
end

IO.read(:stdio, :line)

IO.read(:stdio, :all)
|> String.split("\n")
|> Solution.processData()

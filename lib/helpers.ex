defmodule Helpers do
  def read_lines(str, f) do
    for n <- String.split(str, "\n", trim: true), do: f.(n)
  end
end

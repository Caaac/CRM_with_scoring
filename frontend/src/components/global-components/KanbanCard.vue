<script setup>
</script>

<template>
  <div class="kanban-card">
    <div class="kanban-card-container">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss">
.kanban-card {
  width: calc(var(--kanban-column-width) - var(--kanban-card-gap));
  height: auto;
  background: white;
  border-radius: 10px;
  margin-top: 7px;
  margin-bottom: 8px;

  .kanban-card-container {
    width: 100%;
    height: 100%;
    padding: 7px 7px;
  }
}

.kanban-card:hover {
  cursor: pointer;
  margin-top: 5px;
  margin-bottom: 10px;
}
</style>